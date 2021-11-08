import { createApp } from "vue";
import App from "./App.vue";

import Progress from "ant-design-vue/lib/progress";
import "ant-design-vue/lib/progress/style/index.css";
import Spin from "ant-design-vue/lib/spin";
import "ant-design-vue/lib/spin/style/index.css";
import Drawer from "ant-design-vue/lib/drawer";
import "ant-design-vue/lib/drawer/style/index.css";
import Button from "ant-design-vue/lib/button";
import "ant-design-vue/lib/button/style/index.css";

createApp(App).use(Progress).use(Spin).use(Drawer).use(Button).mount("#app");
