<template>
    <div id="input-modal-overlay" v-if="modalState">
        <div class="input-modal-data">
            <form id="input-form" action="#">
                <div>
                    <span>事件名称</span>
                    <input type="text" v-model="labelName"/>
                </div>
                <br><br>
                <div>
                    <span>其他说明</span>
                    <input type="text" v-model="additionInfo"/>
                </div>
                <br><br>
                <input type="button" @click="submitButton" value="提交"/>
            </form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "inputModal",
        data:function (){
            return {
                modalState:false,
                labelName:"",
                additionInfo:""
            }
        },
        methods:{
            submitButton:function () {
                this.modalState=false;
                this.$emit('add-event',this.labelName);
            },
            showModal:function () {
                this.labelName = "";
                this.additionInfo = "";
                this.modalState=true;
            }
        }
    }
</script>

<style scoped>
    #input-modal-overlay{
        text-align: center;
        z-index: 1000;
        position: absolute;
        left: 0;
        top: 0;
        width:100%;
        height:100%;
        background-color: rgba(0,0,0,0.5);
    }
    #input-form{
        position: relative;
        top: 30%;
    }
    .input-modal-data{
        position: relative;
        top: 35%;
        width: 400px;
        height: 300px;
        text-align: center;
        background-color: white;
        margin: auto;
        border-radius: 25px;
    }
</style>