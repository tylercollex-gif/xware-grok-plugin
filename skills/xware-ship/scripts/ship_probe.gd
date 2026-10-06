extends SceneTree
## XWare ship probe: prints the engine's EFFECTIVE project settings (feature-tag overrides applied).
## <godot> --headless --path <game> -s <abs path>/ship_probe.gd   (no editor, no import, writes nothing)


func _init() -> void:
	var plugins: PackedStringArray = ProjectSettings.get_setting("editor_plugins/enabled", PackedStringArray())
	var autoloads := PackedStringArray()
	for p in ProjectSettings.get_property_list():
		var n: String = p.name
		if n.begins_with("autoload/"):
			autoloads.append(n.trim_prefix("autoload/"))
	print("XWARE_PROBE renderer=%s physics=%s version=%s plugins=%d autoloads=%s" % [
		ProjectSettings.get_setting("rendering/renderer/rendering_method", "forward_plus"),
		str(ProjectSettings.get_setting("physics/3d/physics_engine", "default")).replace(" ", "_"),
		Engine.get_version_info().string.replace(" ", "_"),
		plugins.size(),
		",".join(autoloads) if autoloads.size() > 0 else "-",
	])
	quit(0)
