import { postAction, getAction, deleteAction, putAction } from "./manage"

export const addBook = (param) => postAction("/books/addBook", param)

export const getBooks = (param) => getAction("/books/", param)

export const getBook = (id) => getAction("/books/" + id, null)

export const deleteBook = (id) => deleteAction("/books/" + id, null)

export const changeBookInfo = (id, param) => putAction("/books/" + id, param)