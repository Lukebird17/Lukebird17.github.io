# Personal Academic Homepage

A modern, feature-rich single-page academic homepage built with Hugo, featuring 3D visitor globe, dark mode, and comprehensive analytics.

## ✨ Key Features

### 🎨 Design & UX
- **Single Page Design**: All content on one scrollable page with smooth navigation
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Dark Mode**: Eye-friendly night theme with automatic preference saving
- **Reading Progress Bar**: Visual indicator of scroll progress
- **Fixed Navigation**: Quick access to all sections

### 🌍 Interactive Elements
- **3D Visitor Globe**: Interactive globe showing visitor locations with real-time data
- **Smooth Animations**: Professional hover effects and transitions
- **Mobile-Optimized**: Touch-friendly interface for mobile devices

### 📊 Analytics & Tracking
- **Dual Analytics**: GoatCounter (privacy-friendly) + Google Analytics (detailed insights)
- **Visitor Globe Integration**: Real visitor data displayed on interactive 3D globe
- **Privacy-Focused**: GDPR-compliant tracking options

### 🎓 Academic Focus
- **Publication Management**: Dedicated section with links to papers, code, and projects
- **Research Experience**: Detailed timeline of research activities
- **Professional Profile**: Clean presentation of education, awards, and skills

## 🚀 Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.82.0 or later)
- Git

### Local Development

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/yourusername.github.io.git
cd yourusername.github.io
```

2. **Run development server**:
```bash
hugo server -D
```

3. **Open browser**: Visit `http://localhost:1313`

### Test Features Locally

- 🌍 Click the globe button (bottom right) to open 3D visitor globe
- 🌙 Click the moon button to test dark mode
- 📊 Scroll to see the reading progress bar
- 🔄 Refresh to verify dark mode preference is saved

## 📦 Deployment to GitHub Pages

### Method 1: GitHub Actions (Recommended)

1. **Create repository**: Name it `yourusername.github.io`

2. **Push your code**:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin main
```

3. **Configure GitHub Pages**:
   - Go to repository **Settings** → **Pages**
   - Under **Source**, select **GitHub Actions**

4. **Automatic deployment**: Site builds automatically on push to `main`

5. **Access your site**: `https://yourusername.github.io`

### Method 2: Manual Build

```bash
hugo --minify
# Upload the 'public' folder to your web server
```

## ⚙️ Configuration

### 1. Basic Information

Edit `hugo.toml`:

```toml
[params]
  author = "Your Name"
  description = "Your Homepage Description"
  avatar = "/img/avatar.jpg"
  email = "your@email.com"
  location = "Your City, Country"
  
  [params.social]
    github = "https://github.com/yourusername"
    scholar = "your-google-scholar-url"
    linkedin = "your-linkedin-url"
    twitter = "your-twitter-url"
```

### 2. Avatar

- Place your photo at: `static/img/avatar.jpg`
- Recommended: Square format (500x500px), professional headshot

### 3. Content

Edit `content/_index.md` to update:
- About Me
- Publications
- Research Experience
- Education
- Awards & Services

### 4. Navigation Menu

Modify `hugo.toml`:

```toml
[[menu.main]]
  identifier = "about"
  name = "About"
  url = "#about"
  weight = 1
```

## 📊 Analytics Setup

### Option 1: GoatCounter (Recommended for Privacy)

**Why GoatCounter?**
- ✅ Free and open-source
- ✅ No cookies, GDPR-compliant
- ✅ Provides location data for globe visualization
- ✅ Lightweight and fast

**Setup (5 minutes):**

1. **Sign up**: https://www.goatcounter.com/signup
   - Choose a code (e.g., `lukebird17`)
   - Your dashboard will be at: `https://your-code.goatcounter.com`

2. **Update code** in `layouts/index.html`:
```html
<script data-goatcounter="https://YOUR-CODE.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

3. **Enable API** (for globe data):
   - GoatCounter Dashboard → Settings → API
   - Check "Enable API access"
   - Copy API token

4. **Fetch visitor data** (optional):
```bash
cd /Users/leon/Project/personal-homepage
python3 fetch_goatcounter_data.py
```

### Option 2: Google Analytics (Detailed Insights)

**Setup:**

1. **Create account**: https://analytics.google.com
   - Property name: "Personal Homepage"
   - Website URL: `https://yourusername.github.io`

2. **Get Measurement ID**: Format `G-XXXXXXXXXX`

3. **Update** `layouts/index.html`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Recommended**: Use both! GoatCounter for lightweight tracking + globe data, Google Analytics for detailed insights.

## 🌍 3D Visitor Globe

### Features
- Interactive 3D Earth with real visitor locations
- Automatic rotation with manual control
- Hover to see city names and visit counts
- Real-time statistics (total visits, unique visitors, countries)
- Night sky background in dark mode

### Data Sources

**Current**: Fallback demo data (15 cities)

**Real Data Options**:
1. **GoatCounter API** (recommended):
   - Run `fetch_goatcounter_data.py` to generate `static/visitor-data.json`
   - Updates automatically when deployed

2. **Google Analytics** (advanced):
   - Requires GA4 and additional Python script setup

## 🌙 Dark Mode

### Features
- Night-friendly color scheme (deep slate background + emerald accents)
- Smooth transition animations
- Automatic preference saving
- No flash on page load

### Colors
- **Light Mode**: White background + dark green theme
- **Dark Mode**: Night sky blue (`#0f172a`) + emerald green (`#10b981`)

### Customization

Edit `layouts/index.html` CSS:

```css
[data-theme="dark"] {
    --primary-color: #10b981;     /* Main accent color */
    --bg-main: #0f172a;           /* Background */
    --text-primary: #f1f5f9;      /* Text color */
}
```

## 🎨 Color Scheme

### Light Mode
- Primary: `#01513a` (Forest green)
- Primary Light: `#028760` (Sea green)
- Background: `#ffffff` (White)
- Accent: `#ff9800` (Orange)

### Dark Mode
- Primary: `#10b981` (Emerald)
- Primary Light: `#34d399` (Light emerald)
- Background: `#0f172a` (Midnight blue)
- Secondary BG: `#1e293b` (Slate gray)

## 📁 Project Structure

```
personal-homepage/
├── .github/workflows/
│   └── hugo.yml              # Auto-deployment
├── content/
│   └── _index.md             # Main content
├── layouts/
│   └── index.html            # Main template (with all features)
├── static/
│   ├── img/
│   │   └── avatar.jpg        # Your photo
│   ├── cv.pdf                # Your CV
│   └── visitor-data.json     # Globe data (optional)
├── fetch_goatcounter_data.py # Data fetcher script
├── hugo.toml                 # Site config
└── README.md                 # This file
```

## 🔧 Troubleshooting

### Dark Mode Not Working
1. Clear browser cache: `Cmd/Ctrl + Shift + R`
2. Check browser console for JavaScript errors
3. Verify `localStorage` is enabled in browser

### Globe Not Loading
1. Check browser console for errors
2. Verify `globe.gl` library loaded
3. Test with fallback data first

### Analytics No Data
- **GoatCounter**: Wait 5 minutes, check real-time view
- **Google Analytics**: Wait 24-48 hours for first report, use "Realtime" for instant feedback

### Images Not Loading
1. Place images in `static/` folder
2. Reference with `/img/filename.jpg` (leading slash required)
3. Check file paths are case-sensitive

### Deployment Fails
1. Check GitHub Actions workflow status
2. Verify Hugo version in `.github/workflows/hugo.yml`
3. Ensure repository is public
4. Check that Pages is enabled in Settings

## 💡 Customization Tips

### Add New Section
1. Update `content/_index.md`
2. Add navigation link in `hugo.toml`
3. Style in `layouts/index.html` if needed

### Change Fonts
Edit `layouts/index.html`:
```css
body {
    font-family: 'Your Font', -apple-system, sans-serif;
}
```

### Adjust Button Position
```css
.theme-toggle {
    bottom: 30px;  /* Distance from bottom */
    right: 30px;   /* Distance from right */
}

.globe-toggle {
    bottom: 90px;  /* Stack above theme button */
}
```

## 📱 Mobile Optimization

All features are mobile-friendly:
- ✅ Responsive navigation (hamburger menu on mobile)
- ✅ Touch-friendly buttons (50px minimum tap target)
- ✅ Globe works with touch gestures
- ✅ Dark mode button accessible on small screens
- ✅ Reading progress bar visible on all devices

## 📝 Content Tips

1. **Publications**: Add most important first, include links to papers, code, demos
2. **Avatar**: Use high-quality professional photo, 500x500px recommended
3. **Bio**: Keep concise, link to detailed CV for comprehensive info
4. **SEO**: Update meta description in `hugo.toml` for better search visibility
5. **Loading Speed**: Optimize images (WebP format, < 200KB)

## 🔐 Privacy & GDPR

This template respects user privacy:

- **GoatCounter**: No cookies, no personal data, GDPR-compliant
- **Google Analytics**: Anonymized IP addresses, configurable
- **Optional**: Add privacy policy page in footer

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Hugo](https://gohugo.io/)
- 3D Globe powered by [globe.gl](https://github.com/vasturiano/globe.gl)
- Analytics by [GoatCounter](https://www.goatcounter.com/)
- Inspired by modern academic homepage designs

## 📧 Support

Questions or issues?
- Open an issue on GitHub
- Email: your@email.com

## 🚀 Next Steps

After setup:
1. ✅ Customize content in `content/_index.md`
2. ✅ Add your avatar to `static/img/avatar.jpg`
3. ✅ Configure analytics (GoatCounter + Google Analytics)
4. ✅ Upload CV to `static/cv.pdf`
5. ✅ Test all features locally
6. ✅ Deploy to GitHub Pages
7. ✅ Share your homepage! 🎉

---

**Made with ❤️ for researchers by researchers**
