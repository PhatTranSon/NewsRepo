const express = require("express");
const path = require("path");
const NewsRouter = require("../routes/news.route");
const ErrorHandling = require("../middlware/error_handling");
const cors = require("cors");

//Create express application
const app = express();

//Use cors
app.use(cors());

//API homepage
app.use(express.static("public"));

//Basic route for introducing the application
app.get("/about", (req, resp) => {
    resp.status(200).json({
        about: "This is an RestAPI written to serve news articles scraped from multiple sources. For more information, please visit https://github.com/PhatTranSon/NewsRepo"
    });
});

//Basic routing for news
app.use("/news", ErrorHandling(NewsRouter));

//Run the app
app.listen(process.env.PORT || 5000, () => console.log("Application is running"));
