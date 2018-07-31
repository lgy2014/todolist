<template>
<div>
    <Row>
        <Col span="24">
        <h3>todos</h3>
            <Input v-model="value" @keyup.enter.native="addItem" size="large" placeholder="todo something ..." style="width: 300px"></Input>
            <Item v-bind:todos="todos"></Item>
            <Button type="success" @click.native="clearAll">清除全部</Button>
            <div><span>Copyright © 2018 liugy</span></div>
        </Col>
    </Row>
</div>
</template>
<script>
import Item from "./item.vue";
import Store from "./store"

export default {
  data() {
    return {
      value: "",
      todos: Store.fetch()
    };
  },
  watch:{
      todos:{
          handler:function(){
              Store.save(this.todos);
          },
          deep:true
      }
  },
  components: {
    Item
  },
  methods: {
    addItem: function(event) {
      var item = {text: this.value,isCompleted:false };
      this.todos.unshift(item);
      this.value = "";
    },
    clearAll:function(){
        this.todos.splice(0,this.index);
    }
  }
};
</script>
