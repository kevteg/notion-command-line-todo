# notion-command-line-todo
Add something to your notion TODO list from the command line

<img width="760" alt="A TODO page on notion and the terminal with the TODO command on it" src="https://user-images.githubusercontent.com/5288503/160753789-17d93613-ea89-4379-8e86-d06bf2251a89.png">

## Seting up the notion page

- Create a new [notion integration](https://developers.notion.com/docs/getting-started#step-1-create-an-integration)
- Make sure to share your TODO page with your integration: (Here you have a [simple example](https://keeeevin.notion.site/TODO-f0f9e8f1c35744ee8bf87fa2dd83882a))
<img width="427" alt="Notion share modal" src="https://user-images.githubusercontent.com/5288503/159582677-c1d4c2f5-2d07-44fe-92a1-34ef524f1d20.png">

- Copy the page ID: 
<img width="652" alt="Example image of the page ID" src="https://user-images.githubusercontent.com/5288503/160753469-7deaacfe-1704-4bcc-9a8a-c30924c5ce78.png">


## Running using docker

 - Create the image and tag it:
```
> docker build . -t notion 
```

- Run the command, make sure you have the integration token and the page ID 
```
> docker run -it -v $(pwd):/usr/src/app notion python pytodo.py -t INTEGRATION_TOKEN -p PAGE_ID Buy almond milk
```

- Create an alias, (the command above is a little ugly, isn't it? So I'd rather create an alias on the bashrc/zshrc/equivalent):
```
...
alias todo="docker run -it -v /Your-Directory/notion-command-line-todo:/usr/src/app notion python pytodo.py -t INTEGRATION_TOKEN -p PAGE_ID"
```

Then you can just do this:

```
> todo buy almond milk
```

## Available commands

### Add a new entry: (Default)


```
> todo buy brocoli 
```

### List things in the notion page: 

You will see all the TODO blocks on your notion page

```
> todo -l
> [X] Take out trash
  [] Buy chocolate
  [] Buy broccoli
  [] Run a 5K marathon
```
