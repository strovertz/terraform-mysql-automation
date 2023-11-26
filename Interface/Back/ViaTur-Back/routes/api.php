<?php

use App\Http\Controllers\SupplierController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


Route::middleware('auth:api')->get('/ClientArea', function (Request $request) {
return $request->user();
});

Route::middleware('auth:api')->post('/ClientArea', function (Request $request) {
return $request->user();
});

Route::get('/users', function () {
return response(['opa']);
})->middleware('auth');

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
return $request->user();
});
Route::apiResource('form', SupplierController::class)->only(['store', 'update']);
