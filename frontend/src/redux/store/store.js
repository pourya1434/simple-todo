import { configureStore } from "@reduxjs/toolkit";

import userReducer from "../slice/user/userSlice";

// import reducers
const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

export default store;
