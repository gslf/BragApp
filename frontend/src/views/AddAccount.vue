<template>
  <div class="add-account">
    <h1 class="add-account-title">ADD NEW ACCOUNT</h1>

    <p v-if="message" :class="['add-account-message', messageclass]">{{ message }}</p>

    <form @submit.prevent="addAccount">
      <div class="add-account-form-group">
        <label for="account_number">Account Number</label>
        <input type="number" v-model="account.account_number" required />
      </div>
      <div class="add-account-form-group">
        <label for="account_name">Account Name</label>
        <input type="text" v-model="account.account_name" minlenght="1" maxlenght="100" required />
      </div>
      <div class="add-account-form-group">
        <label for="iban">IBAN</label>
        <input type="text" v-model="account.iban" required />
      </div>
      <div class="add-account-form-group">
        <label for="address">Address</label>
        <input type="text" v-model="account.address" minlenght="1" maxlenght="200" required />
      </div>
      <div class="add-account-form-group">
        <label for="amount">Amount</label>
        <input type="number" v-model="account.amount" min="1" max="999999999999" step="0.01" required />
      </div>
      <div class="add-account-form-group">
        <label for="type">Type</label>
        <select v-model="account.type" required>
          <option value="sending">Sending</option>
          <option value="receiving">Receiving</option>
        </select>
      </div>
      <button type="submit"><i class="pi pi-plus-circle" style="font-size: 1.5rem"></i> ADD ACCOUNT</button>
    </form>
  </div>
</template>
  
<script setup>
  import { ref } from 'vue';

  // Reactive vars
  const account = ref({
    account_number: '',
    account_name: '',
    iban: '',
    address: '',
    amount: 0,
    type: 'sending',
  });

  const message = ref('');
  const messageclass = ref('');

  // API CALL - Add New Account
  const addAccount = async () => {
    try {
      const response = await fetch(import.meta.env.VITE_BRAGAPP_API_BASE_URL + 'accounts/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(account.value),
      });

      const statusCode = response.status;

      if(statusCode === 200){
        const data = await response.text();
        messageclass.value = "success";
        message.value = `Account added successfully. Transaction ID: ${data}.`;
        scrollTop();
        resetForm();
      }else if(statusCode === 422){
        const data = await response.json();
        console.log(data);
        messageclass.value = "error";
        message.value = `Validation Error: ${data["detail"][0]["loc"][1].toUpperCase()} ${data["detail"][0]["msg"]}.`;
        scrollTop();
      }else if(statusCode === 409){
        const data = await response.json();
        console.log(data);
        messageclass.value = "error";
        message.value = `Conflict: Account number must be unique.`;
        scrollTop();
      }else{
        messageclass.value = "error";
        message.value = `Server Error!`;
        scrollTop();
      }
      
    } catch (error) {
      console.error('Error adding account:', error);
      message.value = 'Failed to add account.';
    }
  };

  // Scroll to the top function
  const scrollTop = () => {
    window.scrollTo({
      top: 0, 
      behavior: 'smooth' 
    });
  }

  // Form reset function
  const resetForm = () => {

    // Clear form values
    account.value = {
      account_number: '',
      account_name: '',
      iban: '',
      address: '',
      amount: 0,
      type: 'sending',
    };
  };
</script>

  
<style>
  .add-account {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  

  .add-account-title{
    padding-top: 40px;
    padding-bottom: 20px;
  }

  .add-account form{
    display: flex;
    flex-direction: column;
  }
  
  .add-account-form-group {
    display: flex;
    flex-direction: column;

    margin: 10px 0;
  }
  
  .add-account-form-group input, .add-account-form-group select {
    padding: 8px;
    width: 300px;
    height: 40px;
    margin-top: 5px;
    padding: 5px; 
    box-sizing: border-box; 
    border: 1px solid #ccc; 
  }
  
  .add-account form button{
    display: flex;
    align-items: center;
    justify-content: center;

    width: 300px;
    height:40px;

    color: var(--color-green-dark);
    padding: 8px;
    margin-top: 40px;
  }

  .add-account form button i{
    padding-right: 10px;
  }

  .add-account-message{
    width: 300px;
    margin-top:30px;
    margin-bottom:30px;
  }

  .add-account-message.error{
    color:var(--color-red);
  }

  .add-account-message.success{
    color:var(--color-green);
  }
</style>


  