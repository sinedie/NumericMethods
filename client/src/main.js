import HMR from "@roxi/routify/hmr";
import App from "./App.svelte";

// import { makeServer } from "./server";
// makeServer();

const app = HMR(App, { target: document.body }, "routify-app");

export default app;
