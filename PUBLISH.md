# Publish XWare Grok plugin to GitHub

Local package is ready. Complete these steps on your machine.

## 1. Create empty repo on GitHub

1. Open https://github.com/new  
2. **Name:** `xware-grok-plugin`  
3. **Public**  
4. **Do not** add README, .gitignore, or license  
5. Create repository  
6. Copy the URL, e.g. `https://github.com/YOURUSER/xware-grok-plugin.git`

## 2. Push (PowerShell or Git Bash)

```powershell
cd "C:\Users\winge\Documents\Xware\grok-plugin"

# If not already committed (safe to re-run):
git status

# Point at YOUR repo (replace YOURUSER)
git remote remove origin 2>$null
git remote add origin https://github.com/YOURUSER/xware-grok-plugin.git
git remote -v

git push -u origin main
```

### Auth

- **HTTPS:** use a [Personal Access Token](https://github.com/settings/tokens) as the password  
- **SSH:** `git remote set-url origin git@github.com:YOURUSER/xware-grok-plugin.git`

## 3. After first push

1. Edit `plugin.json` → set `"homepage"` to your real GitHub URL  
2. Commit: `git add plugin.json README.md ; git commit -m "Set homepage URL" ; git push`  
3. On the repo page: **Settings → General → Topics** → add `grok`, `godot`, `gamedev`, `xai`, `plugin`  
4. Note commit SHA for marketplace PR:

```powershell
git rev-parse HEAD
```

## 4. Install from GitHub

```powershell
grok plugin install YOURUSER/xware-grok-plugin --trust
```

## 5. Submit to xAI marketplace

1. Fork https://github.com/xai-org/plugin-marketplace  
2. Add entry in `.grok-plugin/marketplace.json` with your `url` + full `sha`  
3. Run:

```bash
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
```

4. Open a Pull Request  

Details: https://github.com/xai-org/plugin-marketplace#add-or-update-a-plugin
