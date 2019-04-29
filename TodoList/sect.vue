<template>
    <div id="sect">
        <mt-checklist
                v-model="value"
                :options="options">
        </mt-checklist>
        <div v-if="options.length === 0" id="waring-tags">
            <span>没有任何待办事情</span>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import { Checklist } from 'mint-ui';
    Vue.component(Checklist.name, Checklist);
    export default {
        name: 'sect',
        data:function() {
            return {
                value:[],
                options : []
            }
        },
        methods:{
            addContent:function (value) {
                try{
                    this.options.forEach((label,index)=>{
                        if(label === value){
                            throw '待完成事件已经存在了！'
                        }
                    });
                }
                catch (e) {
                    alert(e);
                    return ;
                }
                this.options.push(value);
            }
        }
    }
</script>

<style>
    #waring-tags{
        position: relative;
        top:40%;
        text-align: center;
    }
    #sect{
        text-align: left;
        height: 600px;
    }
</style>