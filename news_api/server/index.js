const express = require("express");
const NewsRouter = require("../routes/news.route");

//Create express application
const app = express();

//Basic routing for news
app.use("/news", NewsRouter);

//Run the app
app.listen(process.env.PORT || 5000, () => console.log("Application is running"));
