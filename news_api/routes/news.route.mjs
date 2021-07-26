import express from "express";

//Create simple router
const router = express.Router();

//Add path
router.get("/", (req, resp, next) => {
    resp.end("News!!!");
});

export default router;