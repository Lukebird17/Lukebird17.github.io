# Personal Homepage

A clean, modern single-page academic homepage built with Hugo.

## 🌟 Features

- **Single Page Design**: All content on one page with smooth scrolling navigation
- **Fixed Top Navigation**: Easy access to all sections
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Clean & Professional**: Academic-focused design with emphasis on publications and research
- **Easy to Customize**: Simple configuration and content management

## 📁 Project Structure

```
personal-homepage/
├── .github/
│   └── workflows/
│       └── hugo.yml          # GitHub Actions deployment
├── content/
│   └── _index.md             # Main page content
├── themes/
│   └── tokiwa-single/
│       ├── layouts/
│       │   └── index.html    # Main template
│       └── theme.toml
├── hugo.toml                 # Site configuration
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.82.0 or later)
- Git

### Local Development

1. Clone this repository:
```bash
git clone https://github.com/Lukebird17/Lukebird17.github.io.git
cd Lukebird17.github.io
```

2. Run the development server:
```bash
hugo server -D
```

3. Open your browser and visit: `http://localhost:1313`

## ✏️ Customization

### 1. Basic Information

Edit `hugo.toml` to update your personal information:

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
    email = "mailto:your@email.com"
```

### 2. Add Your Avatar

Place your profile picture at: `static/img/avatar.jpg`

The image should be:
- Square format (e.g., 500x500px)
- Clear headshot
- Professional appearance

### 3. Update Content

Edit `content/_index.md` to update your:
- About Me section
- Publications
- Experience
- Education
- Services
- Miscellaneous information

Each section uses HTML for better formatting control.

### 4. Navigation Menu

The navigation menu is automatically generated from `hugo.toml`. To modify:

```toml
[[menu.main]]
  identifier = "about"
  name = "About"        # Display name
  url = "#about"        # Link to section
  weight = 1            # Order (lower number = earlier)
```

## 📦 Deployment to GitHub Pages

### Method 1: Using GitHub Actions (Recommended)

1. Create a new repository named: `yourusername.github.io`

2. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin main
```

3. In your GitHub repository:
   - Go to **Settings** → **Pages**
   - Under **Source**, select **GitHub Actions**

4. The site will automatically build and deploy when you push changes to the `main` branch

5. Your site will be available at: `https://yourusername.github.io`

### Method 2: Manual Build

```bash
hugo --minify
# Upload the 'public' folder to your web server
```

## 🎨 Color Scheme

The theme uses a professional green color palette:

- Primary: `#01513a` (Dark green)
- Primary Light: `#028760` (Medium green)
- Background Light: `#edf9f8` (Very light green)
- Accent: `#ff9800` (Orange for badges)

To change colors, edit the `:root` CSS variables in `themes/tokiwa-single/layouts/index.html`.

## 📝 Tips

1. **Publications**: Add the most important publications first. Include links to papers, code, and projects.

2. **Avatar**: Use a high-quality, professional photo. The circular crop works best with centered headshots.

3. **Content Organization**: Keep each section concise. Link to detailed CVs or external pages for comprehensive information.

4. **SEO**: Update the meta description in `hugo.toml` for better search engine visibility.

5. **Mobile**: Test your site on mobile devices to ensure all content is readable.

## 🔧 Troubleshooting

### Site not showing up on GitHub Pages

1. Check that your repository is named correctly: `yourusername.github.io`
2. Ensure GitHub Actions workflow completed successfully
3. Verify Pages settings use "GitHub Actions" as source

### Images not loading

1. Place images in the `static/` folder
2. Reference them with `/img/filename.jpg` (leading slash)
3. Ensure paths are correct and case-sensitive

### Navigation not scrolling

1. Make sure section IDs in content match navigation URLs
2. Example: `<section id="about">` matches `url = "#about"`

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Hugo](https://gohugo.io/)
- Design inspired by modern academic homepages
- Color scheme inspired by the Tokiwa theme

## 📧 Contact

If you have questions or suggestions, feel free to:
- Open an issue on GitHub
- Contact me at: your@email.com

---

**Made with ❤️ by Hongliang Lu**
