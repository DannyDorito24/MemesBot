const { Client, Collection } = require('discord.js');
const fs = require('fs');

const client = new Client();
const login = JSON.parse(fs.readFileSync("login.json"));
const prefix = login.prefix

client.login(login.token);

client
  .on('ready', () => {
    console.log('Bot logged in.');
  })
  // Client message event, contains the logic for the command handler.
  .on('message', (message) => {
    // Make sure the message contains the command prefix from the config.json.
    if (!message.content.startsWith(prefix)) return;
    // Make sure the message author isn't a bot
    if (message.author.bot) return;
    // Make sure the channel the command is called in is a text channel.
    if (message.channel.type !== 'text') return;

    // Split the message content and store the command called, and the args.
    const messageSplit = message.content.split(/\s+/g);
    const cmd = messageSplit[0].slice(prefix.length);
    const args = messageSplit.slice(1);

    if (cmd === "info") {
        message.channel.send("This bot was programmed by DannyDorito ~~using a ton of code from stackoverflow~~ \n \n The commands that can be used are: \n ``!save <name> <url>`` to save a file \n ``!meme <name>`` to recall an image \n ``!list`` to list all memes in the database")
    }

    if (cmd === "earth") {
      message.channel.send("The earth is round.")
    }

    if (cmd === "brassmonkey") {
      const bmonkey = client.emojis.cache.find(emoji => emoji.name === "brassmonkey");
            message.channel.send(`${bmonkey}`);
    }

    if (cmd === "meme") {
      message.channel.send("<@381608421906186240> Go implement this feature you lazy piece of shit");
    }

    if (cmd === "list") {
      message.channel.send("<@381608421906186240> Go implement this feature you lazy piece of shit")
    }

    if (cmd === "save") {
        let name = args.slice(1);
        let url = args.slice(2);

        var obj = {
          table: []
        }

        obj.table.push({name:`${name}`, url:`${url}`});
        var json = JSON.stringify(obj);
        fs.writeFile('./urls.json', json, 'utf8', callback);
        fs.readFile('myjsonfile.json', 'utf8', function readFileCallback(err, data){
          if (err){
              console.log(err);
          } else {
          obj = JSON.parse(data); //now an object
          obj.table.push({name:`${name}`, url:`${url}`}); //add data
          json = JSON.stringify(obj); //convert it back to json
          fs.writeFile('myjsonfile.json', json, 'utf8', callback); // write it back
        }})

  }});