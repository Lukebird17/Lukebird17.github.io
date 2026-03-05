#!/usr/bin/env python3
"""
从 GoatCounter 获取访客地理数据并生成 visitor-data.json

使用方法：
1. 安装依赖：pip install requests
2. 配置你的 GoatCounter 站点代码和 API Token
3. 运行：python fetch_goatcounter_data.py
"""

import requests
import json
from datetime import datetime
from collections import defaultdict

# 配置
GOATCOUNTER_SITE = "lukebird17"  # 替换为你的站点代码，如 "lukebird17"
API_TOKEN = "qr4nfncgcdje1l05y7s9ekget1bwlvojjv08h4195kh7jdnhzdz"    # 从 Settings → Password/API 获取
OUTPUT_FILE = "static/visitor-data.json"

# 主要城市/国家坐标映射
LOCATION_COORDS = {
    # 国家级别（如果没有具体城市）
    "China": {"lat": 35, "lng": 105, "city": "China", "country": "China"},
    "United States": {"lat": 37.0902, "lng": -95.7129, "city": "United States", "country": "United States"},
    "United Kingdom": {"lat": 55.3781, "lng": -3.4360, "city": "United Kingdom", "country": "United Kingdom"},
    "Germany": {"lat": 51.1657, "lng": 10.4515, "city": "Germany", "country": "Germany"},
    "France": {"lat": 46.2276, "lng": 2.2137, "city": "France", "country": "France"},
    "Japan": {"lat": 36.2048, "lng": 138.2529, "city": "Japan", "country": "Japan"},
    "South Korea": {"lat": 35.9078, "lng": 127.7669, "city": "South Korea", "country": "South Korea"},
    "Canada": {"lat": 56.1304, "lng": -106.3468, "city": "Canada", "country": "Canada"},
    "Australia": {"lat": -25.2744, "lng": 133.7751, "city": "Australia", "country": "Australia"},
    "India": {"lat": 20.5937, "lng": 78.9629, "city": "India", "country": "India"},
    "Brazil": {"lat": -14.2350, "lng": -51.9253, "city": "Brazil", "country": "Brazil"},
    "Russia": {"lat": 61.5240, "lng": 105.3188, "city": "Russia", "country": "Russia"},
    "Singapore": {"lat": 1.3521, "lng": 103.8198, "city": "Singapore", "country": "Singapore"},
    "Netherlands": {"lat": 52.1326, "lng": 5.2913, "city": "Netherlands", "country": "Netherlands"},
    "Spain": {"lat": 40.4637, "lng": -3.7492, "city": "Spain", "country": "Spain"},
    "Italy": {"lat": 41.8719, "lng": 12.5674, "city": "Italy", "country": "Italy"},
    
    # 城市级别
    "Shanghai": {"lat": 31.2304, "lng": 121.4737, "city": "Shanghai", "country": "China"},
    "Beijing": {"lat": 39.9042, "lng": 116.4074, "city": "Beijing", "country": "China"},
    "Hong Kong": {"lat": 22.3193, "lng": 114.1694, "city": "Hong Kong", "country": "Hong Kong"},
    "New York": {"lat": 40.7128, "lng": -74.0060, "city": "New York", "country": "United States"},
    "Los Angeles": {"lat": 34.0522, "lng": -118.2437, "city": "Los Angeles", "country": "United States"},
    "San Francisco": {"lat": 37.7749, "lng": -122.4194, "city": "San Francisco", "country": "United States"},
    "London": {"lat": 51.5074, "lng": -0.1278, "city": "London", "country": "United Kingdom"},
    "Paris": {"lat": 48.8566, "lng": 2.3522, "city": "Paris", "country": "France"},
    "Berlin": {"lat": 52.5200, "lng": 13.4050, "city": "Berlin", "country": "Germany"},
    "Tokyo": {"lat": 35.6762, "lng": 139.6503, "city": "Tokyo", "country": "Japan"},
    "Seoul": {"lat": 37.5665, "lng": 126.9780, "city": "Seoul", "country": "South Korea"},
    "Singapore": {"lat": 1.3521, "lng": 103.8198, "city": "Singapore", "country": "Singapore"},
    "Sydney": {"lat": -33.8688, "lng": 151.2093, "city": "Sydney", "country": "Australia"},
    "Toronto": {"lat": 43.6532, "lng": -79.3832, "city": "Toronto", "country": "Canada"},
    "Moscow": {"lat": 55.7558, "lng": 37.6173, "city": "Moscow", "country": "Russia"},
    "Mumbai": {"lat": 19.0760, "lng": 72.8777, "city": "Mumbai", "country": "India"},
    "Amsterdam": {"lat": 52.3676, "lng": 4.9041, "city": "Amsterdam", "country": "Netherlands"},
    "Madrid": {"lat": 40.4168, "lng": -3.7038, "city": "Madrid", "country": "Spain"},
}


def fetch_goatcounter_stats():
    """从 GoatCounter API 获取统计数据"""
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # 根据官方文档，使用 GET 请求和查询参数
    # 文档: https://www.goatcounter.com/help/api
    
    # 1. 获取总体统计
    total_url = f"https://{GOATCOUNTER_SITE}.goatcounter.com/api/v0/stats/total"
    params = {
        "start": "2026-01-14",  # 最近30天
        "end": "2026-02-13"
    }
    
    print(f"   正在请求总体统计: {total_url}")
    total_response = requests.get(total_url, headers=headers, params=params)
    
    if total_response.status_code == 401:
        print("   ❌ API Token 无效")
        print("   请检查 API_TOKEN 是否正确")
        raise Exception("API 认证失败")
    
    if total_response.status_code == 403:
        print("   ❌ API Token 权限不足")
        print("   请确保 Token 有 'Read' 权限")
        raise Exception("API 权限不足")
    
    if total_response.status_code == 404:
        print("   ⚠️  可能原因：")
        print("      1. GOATCOUNTER_SITE 代码错误")
        print("      2. 账号刚注册，还没有访问数据")
        print("      3. 网站还没有部署追踪代码")
        print("\n   💡 建议：先部署网站，等待 24 小时后再运行此脚本")
        raise Exception("GoatCounter 暂无数据")
    
    total_response.raise_for_status()
    total_data = total_response.json()
    print(f"   ✓ 总访问量: {total_data.get('total', 0)}")
    
    # 2. 获取位置统计 (尝试 location 端点)
    location_url = f"https://{GOATCOUNTER_SITE}.goatcounter.com/api/v0/stats/location"
    
    print(f"   正在请求位置统计: {location_url}")
    location_response = requests.get(location_url, headers=headers, params=params)
    
    if location_response.status_code == 200:
        location_data = location_response.json()
        print(f"   ✓ 获取到 {len(location_data.get('stats', []))} 个位置")
        return total_data, location_data
    else:
        print(f"   ⚠️  位置统计端点返回 {location_response.status_code}，尝试备用方案...")
        
        # 备用方案：尝试 locations（复数）
        location_url_alt = f"https://{GOATCOUNTER_SITE}.goatcounter.com/api/v0/stats/locations"
        location_response_alt = requests.get(location_url_alt, headers=headers, params=params)
        
        if location_response_alt.status_code == 200:
            location_data = location_response_alt.json()
            print(f"   ✓ 获取到 {len(location_data.get('stats', []))} 个位置")
            return total_data, location_data
        else:
            print(f"   ⚠️  无法获取位置数据 (状态码: {location_response_alt.status_code})")
            print("   将只使用总体统计")
            return total_data, {"stats": []}


def process_data(total_data, location_data):
    """处理数据并生成 JSON
    
    Args:
        total_data: 总体统计数据（包含 total 字段）
        location_data: 位置统计数据（包含 stats 列表）
    """
    
    if not location_data or 'stats' not in location_data:
        print("   ⚠️  暂无位置数据")
        return {
            "totalVisits": total_data.get('total', 0),
            "uniqueVisitors": int(total_data.get('total', 0) * 0.7),
            "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
            "locations": []
        }
    
    stats = location_data.get('stats', [])
    locations = []
    location_visits = defaultdict(int)
    
    print(f"   处理 {len(stats)} 条位置统计...")
    
    # 处理位置统计数据
    for stat in stats:
        location_name = stat.get('name', '')
        count = stat.get('count', 0)
        
        if not location_name or location_name == 'Unknown':
            continue
        
        # 查找坐标
        coord = None
        
        # 精确匹配
        if location_name in LOCATION_COORDS:
            coord = LOCATION_COORDS[location_name]
        else:
            # 模糊匹配（处理 "Beijing, China" 这样的格式）
            for key in LOCATION_COORDS:
                if key.lower() in location_name.lower() or location_name.lower() in key.lower():
                    coord = LOCATION_COORDS[key]
                    break
        
        if coord:
            key = (coord['lat'], coord['lng'])
            location_visits[key] += count
    
    # 转换为列表
    for (lat, lng), count in location_visits.items():
        # 找回对应的坐标信息
        for coord_info in LOCATION_COORDS.values():
            if coord_info['lat'] == lat and coord_info['lng'] == lng:
                locations.append({
                    "lat": lat,
                    "lng": lng,
                    "city": coord_info["city"],
                    "country": coord_info["country"],
                    "visits": count
                })
                break
    
    # 按访问量排序，取前 30 个
    locations.sort(key=lambda x: x["visits"], reverse=True)
    locations = locations[:30]
    
    # 从总体统计获取数据
    total_visits = total_data.get('total', 0)
    # GoatCounter 没有直接的 unique visitors 字段，使用估算
    unique_visitors = int(total_visits * 0.7) if total_visits > 0 else 0
    
    return {
        "totalVisits": total_visits,
        "uniqueVisitors": unique_visitors,
        "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
        "locations": locations
    }


def main():
    """主函数"""
    
    if GOATCOUNTER_SITE == "YOUR_CODE" or API_TOKEN == "YOUR_API_TOKEN":
        print("❌ 请先配置 GOATCOUNTER_SITE 和 API_TOKEN")
        print("\n配置方法：")
        print("1. 注册 GoatCounter: https://www.goatcounter.com/signup")
        print("2. 获取 API Token: Settings → Password/API")
        print("3. 修改此脚本中的配置")
        return
    
    print("📊 正在从 GoatCounter 获取数据...")
    
    try:
        # 获取数据
        total_data, location_data = fetch_goatcounter_stats()
        
        # 处理数据
        data = process_data(total_data, location_data)
        
        # 保存到 JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ 成功！数据已保存到 {OUTPUT_FILE}")
        print(f"   总访问量: {data['totalVisits']:,}")
        print(f"   独立访客: {data['uniqueVisitors']:,}")
        print(f"   位置数量: {len(data['locations'])}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求错误: {e}")
        print("\n请确保：")
        print("1. GOATCOUNTER_SITE 正确")
        print("2. API_TOKEN 有效")
        print("3. 网络连接正常")
    except Exception as e:
        print(f"❌ 错误: {e}")


if __name__ == "__main__":
    main()
