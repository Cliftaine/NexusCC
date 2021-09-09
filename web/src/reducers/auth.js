import {
    LOGIN_LOADED,
    LOGIN_LOADING,
    AUTH_ERROR,
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    LOGOUT_SUCCESS,
  } from '../actions/types';
  
  const initialState = {
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    isSuperUser: false,
    isLoading: false,
    user: null,
  };
  
  export default function (state = initialState, action) {
    switch (action.type) {
      case LOGIN_LOADING:
        return {
          ...state,
          isLoading: true,
        };
      case LOGIN_LOADED:
        return {
          ...state,
          isAuthenticated: true,
          isLoading: false,
          isSuperUser: action.payload.role,
          user: action.payload.userName,
        };
      case LOGIN_SUCCESS:
        localStorage.setItem('token', action.payload.token);
        return {
          ...state,
          ...action.payload,
          isAuthenticated: true,
          isLoading: false,
        };
      case AUTH_ERROR:
      case LOGIN_FAIL:
      case LOGOUT_SUCCESS:
        localStorage.removeItem('token');
        return {
          ...state,
          token: null,
          user: null,
          isAuthenticated: false,
          isLoading: false,
        };
      default:
        return state;
    }
  }
  
  