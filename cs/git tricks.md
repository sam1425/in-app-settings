# some useful features of git
This trics have been came out from a youtube [video](https://www.youtube.com/watch?v=ecK3EnyGD8o&list=WL&index=8) from a youtuber called Fireship 

- -am = git add 
	* git commit -am 
- --amend = change last commit name
	* git commit --amend -m "name"
- --force = force push to remote
	* git push origin master --force
- revert = revert last changes (save the commit on history)
	- git revert `name`
- stash = remove the changes and save them without comiting
	- git stash
	- git stash save `name`
	- git stash list
	- git stash appy `index (0-to-...)`
	

