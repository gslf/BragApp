<template>
  <nav>
    <div id="nav-title">
      :#/ <span class="bold">Brag</span>App
    </div>

    <ul class="nav-ul">
      <li class="nav-li"><router-link to="/" active-class="nav-active"><i class="pi pi-list" style="font-size: 2rem"></i></router-link></li>
      <li class="nav-li"><router-link to="/add-account" active-class="nav-active"><i class="pi pi-plus-circle" style="font-size: 2rem"></i></router-link></li>
    </ul>
  </nav>
</template>
  
<script setup>
  defineOptions({
    name: 'Navbar'
  });
</script>
  
  <style>
  nav {
    width: 100%;
    height:58px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;

    background-color: var(--color-green);
  }

  #nav-title{
    display: flex;
    align-items: center;
    flex-grow: 1;
    color: var(--vt-c-white);
    font-size: 16pt;
    padding-left:24px;
  }
  
  .nav-ul {
    display: flex;
    justify-content: center;
    flex-grow: 0;

    list-style-type: none;
    padding-right:12px;
  }
  
  .nav-li{
    margin: 0 15px;
  }
  
  .nav-li a {
    display: flex;
    align-items: center;

    color: var(--vt-c-white);
    text-decoration: none;
  }
  
  .nav-li a:hover {
    color:var(--vt-c-white-mute);
  }

  .nav-active{
    color: var(--color-green-dark) !important;
  }
  </style>
  