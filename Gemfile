source "https://rubygems.org"

# GitHub Pages builds this site with the github-pages gem, which pins Jekyll
# and the supported plugin set. Keeping it here means `bundle exec jekyll serve`
# locally matches what GitHub Pages runs in production.
gem "github-pages", group: :jekyll_plugins

gem "webrick"
gem "tzinfo-data"
gem "wdm", "~> 0.1.0" if Gem.win_platform?

group :jekyll_plugins do
  gem "jekyll-sitemap"
  gem "jekyll-feed"
  gem "jekyll-paginate"
  gem "jekyll-include-cache"
  gem "jemoji"
end
