const { Sequelize } = require("sequelize");
const NewsModel = require("../models/news.model");

//Get the variables
const dbName = process.env.DB_NAME || "newsrepo_db";
const dbUser = process.env.DB_USER || "root";
const dbPassword = process.env.DB_PASSWORD || "Rm!t2012781357";
const dbHost = process.env.DB_HOST || "localhost";

//Create sequelize object
const sequelize = new Sequelize(dbName, dbUser, dbPassword, {
    host: dbHost,
    dialect: "mysql",
    pool: {
        maxConnections: 5,
        maxIdleTime: 30
    }
});

//Define models
const modelDefiners = [
    NewsModel
];
modelDefiners.forEach(modelDefiner => modelDefiner(sequelize));

//Export model
module.exports = sequelize;

