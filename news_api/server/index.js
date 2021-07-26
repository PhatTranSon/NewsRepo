import express from "express";

//Create express application
const app = express();

//Basic routing
app.get("/", (req, resp) => resp.end("Hello World"));

//Run the app
app.listen(process.env.PORT || 5000, () => console.log("Application is running"));
