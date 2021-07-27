const express = require("express");
const {
    getAllNews, getOneNews, getByIds
} = require("../controllers/news.controller");

//Create simple router
const router = express.Router();

//Add path
router.get("/all", getAllNews);
router.get("/byid", getByIds);
router.get("/:newsId", getOneNews);

module.exports = router;