<template>
    <div class="modal-overlay" @click.self="close">
      <div class="modal">
        <button class="modal-close-button" @click="close">X</button>
        <h2 class="modal-title">Account Details</h2>
        <p><span class="bold">Account Number:</span> {{ account.account_number }}</p>
        <p><span class="bold">Account Name:</span> {{ account.account_name }}</p>
        <p><span class="bold">IBAN:</span> {{ account.iban }}</p>
        <p><span class="bold">Address:</span> {{ account.address }}</p>
        <p><span class="bold">Amount:</span> {{ account.amount }}</p>
        <p><span class="bold">Type:</span> {{ account.type }}</p>
      </div>
    </div>
  </template>
  
<script setup>
  import { defineProps, defineEmits } from 'vue';
  
  // Props definition
  const props = defineProps({
    account: {
      type: Object,
      required: true
    }
  });
  
  // Events definition
  const emit = defineEmits(['close']);
  
  // Modal closing function
  const close = () => {
    emit('close');
  };
</script>
  
<style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal {
    position: relative;
    width: 100%;
    height:500px;
    max-width: 400px;

    background: var(--vt-c-white);
    color: var(--vt-c-black);
    padding: 20px;
    
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .modal-close-button {
    color: var(--color-green);
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 18pt;
    font-weight: 700;
  }

  .modal-title{
    font-size: 18pt;
    font-weight: 700;
  }
  </style>
  