/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import {createRouter, createWebHistory} from 'vue-router/auto';
import {setupLayouts} from 'virtual:generated-layouts';
import {routes} from 'vue-router/auto-routes';

// Function to modify routes
// Used to set specific layout if default is not used
function modifyRoutes(routes) {
  return routes.map(route => {
    if (route.path === '/login') {
      route.meta = {...(route.meta || {}), layout: 'minimal'};
    }
    return route;
  });
}

// Add the 404 route
const modifiedRoutes = modifyRoutes(routes);
modifiedRoutes.push({
  path: '/:catchAll(.*)',
  component: () => import('@/components/404.vue'),
  meta: {
    layout: 'minimal'
  },
});

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(modifiedRoutes),
});

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
