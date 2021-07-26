const express = require("express");
const NewsRouter = require("../routes/news.route");
const ErrorHandling = require("../middlware/error_handling");

//Create express application
const app = express();

//Basic routing for news
app.use("/news", ErrorHandling(NewsRouter));

//Run the app
app.listen(process.env.PORT || 5000, () => console.log("Application is running"));
