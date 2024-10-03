<template>
  <div class="account-list">
    <h1 class="account-list-title">ACCOUNTS LIST</h1>

    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>

    <ul v-else>
      <li v-for="account in accounts" :key="account.id" @click="selectedAccount = account">
        <i class="pi pi-money-bill" style="font-size: 2rem"></i> {{ account.account_number }}
      </li>
    </ul>  
    
    <div class="pagination" v-if="totalPages > 1">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>

    <AccountModal v-if="selectedAccount" :account="selectedAccount" @close="selectedAccount = null" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import AccountModal from '../components/AccountModal.vue';

// Reactive variables
const accounts = ref([]);
const selectedAccount = ref(null);
const currentPage = ref(1);
const totalPages = ref(1);
const itemsPerPage = 12;
const errorMessage = ref(''); 

// API CALL - Fetch total account count
const fetchTotalAccounts = async () => {
  try {
    errorMessage.value = ''; // Reset error message
    const url = `${import.meta.env.VITE_BRAGAPP_API_BASE_URL}accounts/count`;
    const response = await fetch(url);

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to fetch total accounts');
    }

    const data = await response.text();
    const totalCount = Number(data);

    totalPages.value = Math.ceil(totalCount / itemsPerPage);

    fetchAccounts();
    
  } catch (error) {
    console.error('Error fetching total account count:', error);
    errorMessage.value = error.message || 'Unable to load the total account count. Please try again later.';
  }
};

// API CALL - Request account list with pagination
const fetchAccounts = async (page = 1) => {
  try {
    errorMessage.value = ''; // Reset error message
    const response = await fetch(`${import.meta.env.VITE_BRAGAPP_API_BASE_URL}accounts/?page=${page}&count=${itemsPerPage}`);

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to fetch accounts');
    }

    const data = await response.json();
    accounts.value = data;
  } catch (error) {
    console.error('Error fetching accounts:', error);
    errorMessage.value = error.message || 'Unable to load the accounts. Please try again later.';
  }
};


// Change page
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchAccounts(currentPage.value);
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchAccounts(currentPage.value);
  }
};

// Load account list and total account count on mount
onMounted(() => {
  fetchTotalAccounts();
});
</script>

<style>
  .account-list-title {
    padding-top: 40px;
    padding-bottom: 20px;
  }

  .account-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .account-list ul {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
    width: 90%;
    max-width: 700px;
    list-style-type: none;
    padding: 0;
  }
  
  .account-list ul li {
    display: flex;
    align-items: center;
    width: 180px;
    cursor: pointer;
    background-color: #f2f2f2;
    color: var(--color-green-dark);
    font-size: 16pt;
    padding: 10px;
    margin: 5px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
  }

  .account-list ul li i {
    padding-right: 10px;
  }
  
  .account-list ul li:hover {
    background-color: #ddd;
  }

  .pagination {
    margin-top: 20px;
  }

  .pagination button {
    margin: 0 5px;
  }

  .error-message {
    color: var(--color-red);
    font-weight: bold;
    margin-bottom: 20px;
  }
</style>
