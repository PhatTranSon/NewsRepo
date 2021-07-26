import express from "express";
import NewsRouter from "../routes/news.route.mjs";

//Create express application
const app = express();

//Basic routing for news
app.use("/news", NewsRouter);

//Run the app
app.listen(process.env.PORT || 5000, () => console.log("Application is running"));
