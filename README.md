# Be Heard: X Hacks 2021 Submission
Educate, Enact, Empower. No voice left behind.
![logo](https://cdn.discordapp.com/attachments/863951358284791808/873909093809672222/Presentation.png)
## Inspiration
To say 2020 was an eventful year would be an understatement. More than ever, social activism is at the forefront of global headlines and both social impact investing and activism are rising at astronomical rates. Because of all of this, we have created Be Heard.
Harnessing natural language processing and data powered by global news syndicates, Be Heard is an information services platform that guarantees that every piece of news is easily digestible and ensures that **no one’s** voice goes unheard.

## What it does
Introducing Be Heard. A one-stop destination for issues around the world, Be Heard is the ultimate tool to educate, emphasize, and enact on critical current events. 

Focused on empowerment, our app offers two pathways for users to use our platform. 
### Educate
On the Educate screen, we use the Contextual Web Search API which harnesses webscraped data from the world’s largest news providers to generate a curated news feed based on a user’s interests, including a reading calendar, spotlight section, and recent headlines section.
![beHeard](https://cdn.discordapp.com/attachments/863951358284791808/873909081532928040/promo_material.png)
* First, we have a reading calendar which is intended to hold different articles, podcasts, books, and more for each day of the month.
* Next, we have the spotlighted section, with posts created by other users that align with your interests. This is what makes our app truly special. It’s not just a news app, it’s a platform for people to have their voices heard.
* Lastly, we have a collection of news related to the users interests as well as recent headlines.
### Enact
On the enact pathway, users have a plethora of ways to use their newfound knowledge to make a difference in the world. Here are our list of features: 
* Create Spotlight: Users can pay to create and post their own articles to spread awareness on a topic they are passionate about.
![enact2](https://cdn.discordapp.com/attachments/863951358284791808/873909084418621490/promo_material2.png)
* Email Representatives: Users can email their local representatives about a specific issue with a single click.
* Sign Petitions: Users can easily find and fill out petitions by filtering by topic.
* Generate Linktree: Users can choose various forms of resources to add to a customized Linktree. A Linktree is a common tool used by social activists to gather information all in one place. Our application makes it easy for people to participate in this.
* Generate Infographic: Users can either input their own information or bring in outside sources and let our NLP text summarization model summarize it and then produce a shareable infographic.

## How we built it
Our team decided to use React Native Expo for the frontend and Flask for our backend servers, with one hosted on AWS and MongoDB Atlas as our database. 

![stacked](https://cdn.discordapp.com/attachments/863951358284791808/873909087455285248/Tech_Stack.png)

### Frontend
Our frontend was built as a React Native mobile app using Expo, capable of running on both iOS and Android mobile devices. By sending HTTP requests to our REST API on our backend, we can retrieve news articles relevant to the user.

### Design Flow

![figma](https://cdn.discordapp.com/attachments/863951358284791808/873909089367908362/flow.png)
### Backend
For handling user authorization and database management, we decided to use a Flask  server which we hosted on AWS, using Amazon’s Elastic Beanstalk
This server is connected to a MongoDB Atlas cluster, also hosted on the cloud, where we store user credentials and user-generated content. We also implemented JSON web tokens to authenticate users.

For hosting our ML model, we used another Flask server, this time hosted through DigitalOcean’s Droplets.

### Finances
After conducting market research on possible competitors, we have concluded that Be Heard sits tight at the intersection of the Information Services Space and the Social Media Networking market, giving Be Heard a total Share of Obtainable Market of over 1 million dollars, and provides users with an unparalleled focus on activism and breadth of news. ![stonks](https://cdn.discordapp.com/attachments/863951358284791808/873909091611861032/market_analysis.png)

Taking our costs of operation (Cloud as a Service, Database, API integration) as well as our projected costs with a targeted Monthly Average Users of 25,000, we estimate profitability by Year 3 of operation.

![cash_money](https://cdn.discordapp.com/attachments/863951358284791808/873910029697290270/conclusion.png)
 



## Challenges we ran into
A few hours before the deadline, our server stopped displaying information for the last two sections of our Educate page. Although this was disappointing, we can still tell you that the user could view the entire collection by clicking at the bottom. They could also see an article preview as well as a link to the complete article when they click on the image.

## Accomplishments that we're proud of
Serving a NLP model through Digital Ocean
Configuring our flask server and CI/CD pipeline on AWS
Building a multi-layered app navigation flow
Bringing a high-fidelity mockup to life

## What we learned
- React Native
- MongoDB 
- Flask
- AWS
- Digital Ocean
- Ubuntu OS

## What's next for Be Heard
The Be Heard team is looking forward to completing the implementation of the features on the Enact page. These features include the petition platform, Linktree generator, and a more advanced infographic creator.

We also hope to monetize our app by having sponsored posts for the spotlight section and selling anonymized and aggregated data of what news/topics that users feel are important to them to news providers.

Most importantly, we can’t wait to see the impact this app can have on the world of social activism!

## Deployment
Our deployment is at this link (must open with the Expo Go mobile app): **http://exp://gc-fxb.anonymous.be-heard-frontend.exp.direct:80** 
![expo qr code](https://cdn.discordapp.com/attachments/863951358284791808/873906559778975784/Screen_Shot_2021-08-08_at_5.32.29_AM.png)
