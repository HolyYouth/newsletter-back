<template>
    <div id="asides">
        <mt-cell title="Test1" class="cell-style"></mt-cell>
        <mt-cell title="Test1" class="cell-style"></mt-cell>
        <mt-cell title="Test1" class="cell-style"></mt-cell>
        <mt-cell title="Test1" class="cell-style"></mt-cell>
    </div>
</template>

<script>
    import Vue from 'vue';
    import { Cell } from 'mint-ui';
    Vue.component(Cell.name, Cell);
    export default {
        name: "asides"
    }
</script>

<style scoped>
    #asides{
        text-align: left;
        width: 70px;
        height: 94%;
        background:#26a2ff;
        float: left;
    }
    .cell-style{
        background-color: #26a2ff;
        color: white;
    }
</style>