# Publish XWare Grok plugin to GitHub

Local package is ready. Complete these steps on your machine.

## 1. Create empty repo on GitHub

1. Open https://github.com/new  
2. **Name:** `xware-grok-plugin`  
3. **Public**  
4. **Do not** add README, .gitignore, or license  
5. Create repository  
6. Copy the URL, e.g. `https://github.com/tylercollex-gif/xware-grok-plugin.git`

## 2. Push

```powershell
cd path\to\xware-grok-plugin
git status
git remote add origin https://github.com/tylercollex-gif/xware-grok-plugin.git
git push -u origin main
```

### Auth

- **HTTPS:** use a [Personal Access Token](https://github.com/settings/tokens) as the password  
- **SSH:** `git remote set-url origin git@github.com:tylercollex-gif/xware-grok-plugin.git`

## 3. After first push

1. Set `plugin.json` homepage to the real GitHub URL  
2. Topics: `grok`, `godot`, `gamedev`, `xai`, `plugin`  
3. Note commit SHA for marketplace PR: `git rev-parse HEAD`

## 4. Install from GitHub

```powershell
grok plugin install tylercollex-gif/xware-grok-plugin --trust
```

## 5. Submit to xAI marketplace

1. Fork https://github.com/xai-org/plugin-marketplace  
2. Add entry in `.grok-plugin/marketplace.json` with `url` + full `sha`  
3. `python3 scripts/generate-plugin-index.py` && `python3 scripts/validate-catalog.py`  
4. Open a Pull Request  

**Do not** commit API keys, machine-local absolute paths, or operator security internals.
