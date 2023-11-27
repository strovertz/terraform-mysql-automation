<?php

use App\Http\Controllers\SupplierManagerController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::prefix('supplier')->group(function (){
   Route::get('', [SupplierManagerController::class, 'index']);
   Route::post('',[SupplierManagerController::class, 'store']);
   Route::put('/{id}', [SupplierManagerController::class, 'update']);
   Route::delete('/{id}',[SupplierManagerController::class, 'delete']);
});
