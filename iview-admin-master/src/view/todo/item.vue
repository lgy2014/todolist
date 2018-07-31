<template>
<div>
    正在进行
<ul>
    <li 
    v-for="(todo,index) in todos"
    v-if="!todo.isCompleted" 
    :index="index"
><Checkbox v-model="todo.isCompleted">{{todo.text}}</Checkbox><Button type="ghost" size="small" @click.native="todos.splice(index,1)" shape="circle" icon="android-remove"></Button></li>
</ul>
已完成
<ul>
    <li 
    v-for="(todo,index) in todos"
    v-if="todo.isCompleted" 
    :index="index"
><Checkbox v-model="todo.isCompleted">{{todo.text}}</Checkbox><Button type="ghost" size="small" @click.native="todos.splice(index,1)" shape="circle" icon="android-remove"></Button></li>
</ul>
</div>
</template>

<script>
export default {
  props: {
    todos: Array
  },
  methods: {
  }
};
</script>
<style>
ul {
  list-style: none;
}
</style>
