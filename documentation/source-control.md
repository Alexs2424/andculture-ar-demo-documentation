# Source Control
> Unfortunately a lot of bad things happen when you use git with Unity projects. Von Bock and I tried multiple ways to get git repos to work but the way the files are setup, there's no easy solution. 

Unity has built in source control underneath the "Collab" Panel. (See Below) ![Collab Panel](images/collab-panel.png) It allows you to commit things to source and collaborate with others but purely through the UI Features. *Note:* There are a lot of aspects in Unity where there aren't controlled by code or traditional ways of interacting with Development tools.

There is a work-around however, you can take all of your C# scripts and put those into a separate github/bitbucket repo. The problem with this is that scripts in Unity do not follow conventional programming concepts in C#. You manipulate the Unity GameObjects with Unity specific functions not traditional C# functions. 
Whole point being, there's not really any reason to completely separate the scripts from the Unity project in their own repo. 

With Unity's source control, they do not defaultly support branches (this may change in time).