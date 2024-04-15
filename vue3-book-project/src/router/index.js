import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/books',
        component: () => import ("@/components/layout.vue")
    },
    {
        path: '/test',
        component: () => import ("@/views/books/BookTest.vue")
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router