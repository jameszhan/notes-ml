
```bash
find . -name "*.csv" -exec ls -lh {} \;

git lfs track "*.csv"
git lfs track "*.zip"
git lfs track "*.tar.gz"

git lfs track

git lfs ls-files
```