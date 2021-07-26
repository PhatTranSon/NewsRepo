const express = require("express");
const {
    getNews
} = require("../controllers/news.controller");

//Create simple router
const router = express.Router();

//Add path
router.get("/", getNews);

module.exports = router;