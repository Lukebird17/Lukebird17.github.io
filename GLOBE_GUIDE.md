# 🌍 3D 访客地球仪使用指南

## ✨ 功能介绍

你的主页现在有一个超酷的 **3D 交互式地球仪**，可以可视化展示全球访客来源！

### 主要特点

- 🌍 **3D 旋转地球** - 真实的地球纹理，自动旋转
- ✨ **发光标记点** - 不同大小代表访问量多少
- 🌊 **波纹动画** - 从访客位置发出的动态波纹
- 🎯 **交互式** - 可以拖动旋转、滚轮缩放
- 📊 **实时统计** - 显示总访问量、独立访客、国家数量
- 🌙 **夜景模式** - 暗黑模式下显示星空背景

## 🎮 如何使用

### 打开地球仪

1. 访问你的主页
2. 看到右下角两个悬浮按钮
   - 🌙 = 暗黑模式切换
   - 🌍 = 访客地球仪
3. 点击 🌍 按钮

### 交互操作

- **拖动鼠标** - 旋转地球
- **滚轮** - 放大/缩小
- **悬停标记点** - 查看城市名称和访问量
- **点击外部** 或 **点击 ✕** - 关闭地球仪

### 查看统计

地球仪底部显示：
- **Total Visits** - 总访问量
- **Unique Visitors** - 独立访客数
- **Countries** - 访问国家数量

## 🎨 视觉效果

### 亮色模式
- 蓝色地球 + 绿色标记点
- 白色背景弹窗

### 暗黑模式（夜景风格）
- 蓝色地球 + 亮绿色标记点
- 深色背景 + 星空
- 发光的统计数字

## 📊 当前数据

目前使用的是 **模拟数据**，包含 15 个主要城市：

| 城市 | 国家 | 访问量 |
|------|------|--------|
| Shanghai | China | 523 |
| New York | USA | 421 |
| Beijing | China | 234 |
| London | UK | 198 |
| San Francisco | USA | 187 |
| Paris | France | 156 |
| Singapore | Singapore | 145 |
| Tokyo | Japan | 134 |
| Moscow | Russia | 112 |
| Berlin | Germany | 98 |
| ... | ... | ... |

**总访问量**：约 2,500+  
**覆盖国家**：15 个

## 🔌 连接真实数据（可选）

### 方法 1：使用 Google Analytics API（推荐）

需要创建一个简单的后端 API 来获取 GA 数据：

1. **设置 Google Analytics API**
   - 访问：https://console.cloud.google.com/
   - 创建新项目
   - 启用 Google Analytics Data API
   - 创建服务账号并下载凭据

2. **创建后端 API**
   - 使用 Node.js/Python/PHP 等
   - 部署到 Vercel/Netlify Functions/Cloudflare Workers
   - API 返回格式：
   ```json
   [
     {
       "lat": 31.2304,
       "lng": 121.4737,
       "city": "Shanghai",
       "country": "China",
       "visits": 523
     }
   ]
   ```

3. **更新前端代码**
   在 `/layouts/index.html` 中找到：
   ```javascript
   const visitorData = [
     // 模拟数据
   ];
   ```
   
   替换为：
   ```javascript
   const visitorData = await fetch('/api/visitor-data')
     .then(res => res.json())
     .catch(() => mockData); // 失败时使用模拟数据
   ```

### 方法 2：手动更新数据

1. 定期从 Google Analytics 导出数据
2. 整理成 JSON 格式
3. 更新 `visitorData` 数组

### 方法 3：使用第三方服务

- **Plausible Analytics** - 提供简单的 API
- **Umami** - 开源、自托管、有 API
- **Simple Analytics** - 注重隐私、有 API

## 🎨 自定义样式

### 修改标记点颜色

在 `index.html` 中找到：
```javascript
.pointColor(d => {
    const intensity = d.visits / 523;
    return `rgba(16, 185, 129, ${0.3 + intensity * 0.7})`;
})
```

修改 RGB 值来改变颜色。

### 修改地球纹理

更换地球图片 URL：
```javascript
.globeImageUrl('你的图片URL')
.bumpImageUrl('你的凹凸图URL')
```

### 调整旋转速度

```javascript
globeInstance.controls().autoRotateSpeed = 0.5; // 0.5 改为其他值
```

## 📱 移动端适配

地球仪已经完全适配移动设备：
- 自动调整大小
- 触摸拖动
- 统计信息竖向排列

## 🐛 故障排除

### 地球仪不显示？

1. **检查浏览器控制台**：F12 查看错误
2. **清除缓存**：Cmd+Shift+R 强制刷新
3. **检查网络**：Globe.gl 需要从 CDN 加载

### 标记点位置不准？

确保纬度（lat）和经度（lng）正确：
- 纬度：-90 到 90
- 经度：-180 到 180

### 地球仪卡顿？

1. 减少数据点数量（推荐 < 50 个）
2. 降低波纹动画频率
3. 关闭自动旋转

## 🚀 性能优化

当前配置已经优化：
- 延迟加载（点击时才初始化）
- 适量数据点（15 个）
- 合理的动画参数

如果访客数据超过 100 个城市，建议：
1. 只显示访问量 Top 50
2. 或者聚合同一国家的数据

## 💡 未来增强功能

可以考虑添加：

1. **访客路径动画** - 显示访客从哪里来
2. **时间轴** - 显示不同时间段的访客分布
3. **热力图** - 用颜色深浅表示访问密度
4. **国家/城市筛选** - 点击标记点显示详细信息
5. **实时更新** - WebSocket 推送新访客
6. **访问趋势** - 显示访问量增长曲线

## 🎉 展示效果

这个 3D 地球仪会：
- ✅ 立即吸引访客注意
- ✅ 展示你的技术能力
- ✅ 让主页更加国际化
- ✅ 提供有趣的交互体验
- ✅ 非常适合学术主页

## 📸 截图建议

把地球仪截图放到：
- GitHub README
- 个人简历
- 社交媒体
- 学术海报

这是一个很好的展示项目！

---

享受你的 3D 访客地球仪吧！🌍✨
