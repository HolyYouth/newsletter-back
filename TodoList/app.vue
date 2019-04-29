<template>
    <div>
        <input-modal ref="event" @add-event="user_input"></input-modal>
        <div id="container">
            <navi @btn-clicked="btn_clicked"></navi>
            <asides v-if="isConfigButtonClicked"></asides>
            <sect ref="input"></sect>
        </div>
    </div>
</template>

<script>
    import Navi from './navi'
    import Sect from './sect'
    import Asides from './asides'
    import InputModal from "./inputModal";
    import 'mint-ui/lib/style.css';
    export default {
        name: "app",
        components: {InputModal, Sect, Asides, Navi},
        data:function() {
            return {
                isConfigButtonClicked:false,
            }
        },
        methods:{
            btn_clicked:function (value) {
                if(value === 'add'){
                    this.$refs.event.showModal();
                }
                else if(value === 'config'){
                    this.isConfigButtonClicked = !this.isConfigButtonClicked;
                }
                else{
                    alert('Unhandled Event!');
                }
            },
            user_input:function (input) {
                this.$refs.input.addContent(input);
            }
        }
    }
</script>

<style scoped>
    div{
        margin:auto;
        text-align: center;
    }
    #container{
        height: 700px;
        width: 400px;
        background: white;
    }
</style>