import { Sequelize } from "sequelize";
import NewsModel from "./news.model";

//Get the variables
const dbName = process.env.DB_NAME;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
const dbHost = process.env.DB_HOST;

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
export default sequelize;

