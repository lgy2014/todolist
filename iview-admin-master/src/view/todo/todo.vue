<template>
<div>
    <Row type="flex" justify="center">
        <Col span="16">
            <h1 class="h1">todo list</h1>
            <Input v-model="value" @keyup.enter.native="addItem" size="large" placeholder="todo something ..." style=""></Input>
            <br />
            <Item v-bind:todos="todos"></Item>
            <br />
            <hr />
            <div style="text-align:right;"><Button type="success" @click.native="clearAll">清除全部</Button></div>
            <br />
            <div style="text-align:center;"><span>Copyright © 2018 liugy</span></div>
        </Col>
    </Row>
</div>
</template>
<script>
import Item from "./item.vue";
import Store from "./store";

export default {
  data() {
    return {
      value: "",
      todos: Store.fetch()
    };
  },
  watch: {
    todos: {
      handler: function() {
        Store.save(this.todos);
      },
      deep: true
    }
  },
  components: {
    Item
  },
  methods: {
    addItem: function(event) {
      if (this.value === "") {
        alert("内容不能为空");
        return;
      }
      var item = { text: this.value, isCompleted: false };
      this.todos.unshift(item);
      this.value = "";
    },
    clearAll: function() {
      this.todos.splice(0, this.index);
    }
  }
};
</script>
<style>
.h1 {
  text-align: center;
}
</style>
