// Vue
import { createApp } from "vue";
import App from "../App.vue";

// Styles
import "../scss/styles.scss";
import "~bootstrap/dist/js/bootstrap.bundle.js";
import "./theme-toggle.js";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import { faBars, faCircleHalfStroke } from "@fortawesome/free-solid-svg-icons";
import { faSun, faMoon } from "@fortawesome/free-regular-svg-icons";

/* add icons to the library */
library.add(faBars, faSun, faMoon, faCircleHalfStroke);

createApp(App).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
