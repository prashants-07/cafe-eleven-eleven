# Café Eleven Eleven — Phase 1 static demo

Six HTML pages, CSS3 and vanilla JavaScript. No backend, npm install, database, or runtime build needed.

## Preview
Open index.html directly, or run python -m http.server 8080 inside this folder.

## Original logo
Copy the supplied original logo to **assets/images/logo/logo.png**. It is used unchanged in header, mobile header, footer, About and favicon. Until supplied, image slots stay hidden and the business name appears as ordinary text. No replacement logo was generated. A missing favicon request is expected until this asset is provided.

## Editing
Menu items, descriptions, prices (null means omitted), categories, image basenames and featured selections are in assets/js/menu-data.js. Update gallery entries in assets/js/gallery.js. Shared navigation/footer live in assets/js/main.js. Page prose is in the individual HTML files. Replace local JPEGs with client-approved photographs retaining filenames or update the paths.
Optional phone, WhatsApp, hours, address and Swiggy fields are reserved in the data file; rendering links for those requires updating contact.html and order.html after confirmation. All existing external links use the supplied references.

## Content status
The name and Sinnar location are supplied by the client. Reference URLs could not be fetched for independent verification. All menu items are samples with no claimed prices or bestseller status. All photographs are illustrative, not this café. The social moodboard is not a set of Instagram posts. Marketing copy is draft. Street address, hours and phone await confirmation. The location graphic is decorative with a real external Maps link, not an embedded map. No fake checkout or contact form exists.

## GitHub Pages
1. Create a GitHub repository.
2. Upload the CONTENTS of this folder to the repository root, including index.html, assets and .nojekyll. Alternatively initialize Git here, commit, add your remote and push to main.
3. Open repository Settings > Pages.
4. Choose Deploy from a branch, main, and / (root), then Save.
5. Wait for deployment and copy the live URL from Settings > Pages.
6. Edit files and push/commit to main to publish future updates.
Relative navigation and asset paths support GitHub project repository URLs. No repository or deployment was created.

## SEO after deployment URL is known
Run: python scripts/configure_seo.py https://YOUR-ACCOUNT.github.io/YOUR-REPOSITORY
Then commit the changed files. The script writes absolute canonical URLs, Open Graph URL/image tags, sitemap entries and the robots sitemap reference. The initial sitemap is intentionally empty; no unknown domain is invented. Python is optional setup tooling, not a website dependency.

## Images
Demo photographs are stored locally from Unsplash. PHOTO-CREDITS.json records source photo IDs (https://images.unsplash.com/photo-ID). The mocktail source returned 404 and was replaced with the beverage photograph. Replace demo images with approved client assets before production. Google Fonts has a system font fallback.

## Accessibility and motion
Keyboard-friendly menu buttons and filters, lightbox with Escape/arrows/focus trapping and focus restoration, reduced-motion support, visible focus rings, skip link and alt text. Shared navigation and interactive grids need JavaScript; basic navigation appears in noscript.
