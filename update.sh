python3 regenerate
bundle exec jekyll build
export WEBWEBPAGE_COMMIT_MESSAGE_DATE_STRING=$(date)
git add .
git commit -m "$WEBWEBPAGE_COMMIT_MESSAGE_DATE_STRING - site generator update"
git push
cd _site
git add .
git commit -m "$WEBWEBPAGE_COMMIT_MESSAGE_DATE_STRING - site update"
git push -f
cd ..
