const routes = [
  {
    path: ["/", "/home"],
    exact: true,
    component: "Home",
  },
  {
    path: ["/upload"],
    exact: true,
    component: "Upload",
  },
  {
    path: ["/download"],
    exact: true,
    component: "Download",
  },
];

export default routes;
