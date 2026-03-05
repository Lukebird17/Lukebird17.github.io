#!/usr/bin/env python3
"""
从 Google Analytics 获取访客地理数据并生成 visitor-data.json

使用方法：
1. 安装依赖：pip install google-analytics-data
2. 配置服务账号凭据（见下方说明）
3. 运行：python fetch_ga_data.py
"""

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import json
from datetime import datetime

# 配置
PROPERTY_ID = "YOUR_GA4_PROPERTY_ID"  # 替换为你的 GA4 Property ID
OUTPUT_FILE = "static/visitor-data.json"

# 主要城市坐标映射（用于将 GA 的城市名转换为经纬度）
CITY_COORDS = {
    "Shanghai": {"lat": 31.2304, "lng": 121.4737, "country": "China"},
    "Beijing": {"lat": 39.9042, "lng": 116.4074, "country": "China"},
    "New York": {"lat": 40.7128, "lng": -74.0060, "country": "United States"},
    "Los Angeles": {"lat": 34.0522, "lng": -118.2437, "country": "United States"},
    "San Francisco": {"lat": 37.7749, "lng": -122.4194, "country": "United States"},
    "London": {"lat": 51.5074, "lng": -0.1278, "country": "United Kingdom"},
    "Paris": {"lat": 48.8566, "lng": 2.3522, "country": "France"},
    "Berlin": {"lat": 52.5200, "lng": 13.4050, "country": "Germany"},
    "Tokyo": {"lat": 35.6762, "lng": 139.6503, "country": "Japan"},
    "Seoul": {"lat": 37.5665, "lng": 126.9780, "country": "South Korea"},
    "Singapore": {"lat": 1.3521, "lng": 103.8198, "country": "Singapore"},
    "Sydney": {"lat": -33.8688, "lng": 151.2093, "country": "Australia"},
    "Toronto": {"lat": 43.6532, "lng": -79.3832, "country": "Canada"},
    "Moscow": {"lat": 55.7558, "lng": 37.6173, "country": "Russia"},
    "Mumbai": {"lat": 19.0760, "lng": 72.8777, "country": "India"},
    "New Delhi": {"lat": 28.6139, "lng": 77.2090, "country": "India"},
    "São Paulo": {"lat": -23.5505, "lng": -46.6333, "country": "Brazil"},
    "Hong Kong": {"lat": 22.3193, "lng": 114.1694, "country": "Hong Kong"},
    "Amsterdam": {"lat": 52.3676, "lng": 4.9041, "country": "Netherlands"},
    "Madrid": {"lat": 40.4168, "lng": -3.7038, "country": "Spain"},
    # 添加更多城市...
}


def fetch_ga_data():
    """从 Google Analytics 获取数据"""
    
    # 初始化客户端（需要设置 GOOGLE_APPLICATION_CREDENTIALS 环境变量）
    client = BetaAnalyticsDataClient()
    
    # 创建请求
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[
            Dimension(name="city"),
            Dimension(name="country"),
        ],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
        ],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )
    
    # 执行请求
    response = client.run_report(request)
    
    return response


def process_data(response):
    """处理 GA 数据并生成 JSON"""
    
    locations = []
    total_visits = 0
    unique_visitors = 0
    
    for row in response.rows:
        city = row.dimension_values[0].value
        country = row.dimension_values[1].value
        active_users = int(row.metric_values[0].value)
        sessions = int(row.metric_values[1].value)
        
        # 只处理有坐标映射的城市
        if city in CITY_COORDS:
            coord = CITY_COORDS[city]
            locations.append({
                "lat": coord["lat"],
                "lng": coord["lng"],
                "city": city,
                "country": country,
                "visits": sessions
            })
            
            total_visits += sessions
            unique_visitors += active_users
    
    # 按访问量排序，取前 30 个
    locations.sort(key=lambda x: x["visits"], reverse=True)
    locations = locations[:30]
    
    return {
        "totalVisits": total_visits,
        "uniqueVisitors": unique_visitors,
        "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
        "locations": locations
    }


def main():
    """主函数"""
    
    print("📊 正在从 Google Analytics 获取数据...")
    
    try:
        # 获取数据
        response = fetch_ga_data()
        
        # 处理数据
        data = process_data(response)
        
        # 保存到 JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ 成功！数据已保存到 {OUTPUT_FILE}")
        print(f"   总访问量: {data['totalVisits']:,}")
        print(f"   独立访客: {data['uniqueVisitors']:,}")
        print(f"   城市数量: {len(data['locations'])}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        print("\n请确保：")
        print("1. 已安装 google-analytics-data: pip install google-analytics-data")
        print("2. 已设置 GOOGLE_APPLICATION_CREDENTIALS 环境变量")
        print("3. PROPERTY_ID 正确")


if __name__ == "__main__":
    main()
