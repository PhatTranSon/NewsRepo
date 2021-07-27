const express = require("express");
const {
    getAllNews, getOneNews
} = require("../controllers/news.controller");

//Create simple router
const router = express.Router();

//Add path
router.get("/:newsId", getOneNews)
router.get("/", getAllNews);

module.exports = router;