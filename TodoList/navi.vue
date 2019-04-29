<template>
    <div id="navi">
        <mt-header title="Todo v0.1">
            <mt-button id="config-button" type="primary" slot="left" @click="$emit('btn-clicked','config')">设置</mt-button>
            <mt-button id="add-button" type="danger" slot="right" @click="$emit('btn-clicked','add')">添加</mt-button>
        </mt-header>
    </div>
</template>

<script>
    import Vue from 'vue'
    import { Button , Header} from 'mint-ui';
    Vue.component(Button.name, Button);
    Vue.component(Header.name, Header);
    export default {
        name: "navi"
    }
</script>

<style scoped>
    #config-button{
        float: left;
    }
    #add-button{
        float: right;
    }
</style>