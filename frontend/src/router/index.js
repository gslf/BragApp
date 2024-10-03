import { createRouter, createWebHistory } from 'vue-router'
import AccountList from '../views/AccountList.vue';
import AddAccount from '../views/AddAccount.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'AccountList',
      component: AccountList
    },
    {
      path: '/add-account',
      name: 'AddAccount',
      component: AddAccount
    }
  ]
})

export default router
