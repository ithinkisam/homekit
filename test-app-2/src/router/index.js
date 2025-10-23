import { createRouter, createWebHistory } from "vue-router";

import AboutPage from "../views/AboutPage";
import AppHome from "../views/AppHome";

const routes = [
  {
    path: "/",
    name: "Home",
    component: AppHome,
  },
  {
    path: "/about",
    name: "About",
    component: AboutPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
