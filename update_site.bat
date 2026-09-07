@echo off
echo Converting txt files to html...
python convert.py

echo Rebuilding search index...
npx pagefind --site .

echo Pushing to GitHub...
git add .
git commit -m "Update site with new content"
git push

echo Done!
pause