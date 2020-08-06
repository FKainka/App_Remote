config.cfg
btree for WLAN -> or stayed saved?

Git Repro with submodules?
Main JSON -> Sets. Points to JSON of Sets

Main JSON
->Main.md

Set.JSON
MainSet.MD

Points to Every JSON in document?


Project:
Readme.md 
\pics
__init__.py
x.py
requirements.txt
\lib
\www


onboard:
\apps\smarthome\p1_1\ as app


config: program -> apps\smarthome\p1_1\ (includes __init__)

\app (main)\ submodules () \ program
			 \ users -> \ sub users \ program

class gitmanger{
	list_manager -> list[] with pop & pull (just the jsons) json stack
		
	
}

git_manager(starturl)
.update() -> get files from web to local
.show() -> get main.json, list Names of Submodules (name: path, relative?)
.info() -> show main.md, (from list.json)
.get(nr).got() -> get Submodule
.install() -> install submodule, resolve requirements
.where(local,url) 	-> show path
.back() 	-> goto before ?
.activate (nr, (auto activate)

name -> path und submoule path
type 0 = set
readme trivial

app.json:
	name		()
	url 		() for update
	path		() local path
	type 		() app\subfolderde
	readme -> file  (open when info)
	files [__init__.py]   (to download)
	requirements []
	
submodule.json
	name 
	url 		() for update
	path		() local path
	type : subfolder
	readme ->
	submodules\apps[] -> links to json
	auto_update 
	auto_activate
	
	
	

